<script setup>
import { onMounted, ref } from "vue";
import { getDashboardSummary } from "./api.js";
import { __ } from "./translate.js";
import KpiHeader from "./components/KpiHeader.vue";
import CompatibilityGrid from "./components/CompatibilityGrid.vue";
import TabCodeScanner from "./components/TabCodeScanner.vue";
import TabStrategyPlanner from "./components/TabStrategyPlanner.vue";

const activeTab = ref("scanner");
const targetVersion = ref("");
const loading = ref(false);
const error = ref("");
const summary = ref(null);

async function loadSummary() {
	loading.value = true;
	error.value = "";
	try {
		summary.value = await getDashboardSummary(targetVersion.value || null);
		if (!targetVersion.value) {
			targetVersion.value = String(summary.value.target_major);
		}
	} catch (err) {
		error.value = err?.message || String(err);
	} finally {
		loading.value = false;
	}
}

onMounted(() => {
	loadSummary();
});
</script>

<template>
	<div class="upgrade-lens-dashboard">
		<div class="ul-toolbar">
			<div class="form-group">
				<label class="control-label">{{ __("Target Major Version") }}</label>
				<input
					v-model="targetVersion"
					type="text"
					class="form-control"
					placeholder="17"
					@keyup.enter="loadSummary"
				/>
			</div>
			<button class="btn btn-primary btn-sm" :disabled="loading" @click="loadSummary">
				{{ loading ? __("Scanning...") : __("Run Scan") }}
			</button>
		</div>

		<div v-if="error" class="alert alert-danger ul-error" role="alert">{{ error }}</div>

		<div v-if="loading && !summary" class="ul-loading">
			<div class="spinner-border spinner text-muted" role="status" />
			<div>{{ __("Analyzing environment...") }}</div>
		</div>

		<template v-if="summary">
			<KpiHeader :summary="summary" />

			<div class="ul-section-label">{{ __("Infrastructure Compatibility") }}</div>
			<CompatibilityGrid :checks="summary.strategy?.infra_checks || []" />

			<div class="ul-tabs">
				<button :class="{ active: activeTab === 'scanner' }" @click="activeTab = 'scanner'">
					{{ __("Code & Schema Scanner") }}
				</button>
				<button :class="{ active: activeTab === 'strategy' }" @click="activeTab = 'strategy'">
					{{ __("Strategy Planner") }}
				</button>
			</div>

			<TabCodeScanner
				v-if="activeTab === 'scanner'"
				:conflicts="summary.conflicts"
				:apps="summary.apps"
			/>
			<TabStrategyPlanner v-else :strategy="summary.strategy" />
		</template>
	</div>
</template>

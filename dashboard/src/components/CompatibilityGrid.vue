<script setup>
import { __ } from "../translate.js";

defineProps({
	checks: { type: Array, default: () => [] },
});

const passedCount = (checks) => checks.filter((c) => c.passed).length;
</script>

<template>
	<div class="form-section">
		<div class="section-body">
			<div v-if="checks.length" class="text-muted text-small margin-bottom">
				{{ passedCount(checks) }}/{{ checks.length }} {{ __("checks passed") }}
			</div>
			<table class="table table-bordered">
				<thead>
					<tr>
						<th>{{ __("Component") }}</th>
						<th>{{ __("Required") }}</th>
						<th>{{ __("Detected") }}</th>
						<th style="width: 100px">{{ __("Status") }}</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="check in checks" :key="check.key">
						<td class="text-capitalize">{{ check.key }}</td>
						<td><code>{{ check.required }}</code></td>
						<td><code>{{ check.actual || "n/a" }}</code></td>
						<td>
							<span
								class="indicator-pill no-indicator-dot"
								:class="check.passed ? 'green' : 'red'"
							>
								{{ check.passed ? __("Pass") : __("Fail") }}
							</span>
						</td>
					</tr>
					<tr v-if="!checks.length">
						<td colspan="4" class="text-muted text-center">
							{{ __("No infrastructure requirements loaded.") }}
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>

<script setup>
import { __ } from "../translate.js";

defineProps({
	strategy: { type: Object, default: () => ({}) },
});

function copyCommands(commands) {
	const text = (commands || []).join("\n");
	frappe.utils.copy_to_clipboard(text);
	frappe.show_alert({ message: __("Commands copied"), indicator: "green" });
}
</script>

<template>
	<div class="widget-group">
		<div
			v-for="path in strategy.paths || []"
			:key="path.id"
			class="ul-path-card"
			:class="{ recommended: path.recommended }"
		>
			<h4>
				{{ path.title }}
				<span
					v-if="path.recommended"
					class="indicator-pill no-indicator-dot green margin-left"
				>
					{{ __("Recommended") }}
				</span>
			</h4>
			<p>{{ path.description }}</p>
			<ul class="checklist">
				<li v-for="item in path.checklist || []" :key="item">{{ item }}</li>
			</ul>
			<pre class="ul-commands">{{ (path.commands || []).join("\n") }}</pre>
			<button class="btn btn-default btn-sm" @click="copyCommands(path.commands)">
				{{ __("Copy Commands") }}
			</button>
		</div>
		<div v-if="!strategy.paths?.length" class="ul-empty">
			{{ __("No migration paths available for this scan.") }}
		</div>
	</div>
</template>

<script setup>
import { __ } from "../translate.js";

defineProps({
	level: { type: String, default: "Low" },
	score: { type: Number, default: 0 },
});

const indicatorClass = {
	Low: "green",
	Medium: "orange",
	High: "red",
};
</script>

<template>
	<span
		class="indicator-pill no-indicator-dot filterable ellipsis"
		:class="indicatorClass[level] || 'green'"
	>
		{{ level }} · {{ __("Score") }} {{ score }}
	</span>
</template>

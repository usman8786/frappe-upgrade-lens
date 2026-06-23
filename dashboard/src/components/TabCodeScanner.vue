<script setup>
import { __ } from "../translate.js";

const props = defineProps({
	conflicts: { type: Object, default: () => ({}) },
	apps: { type: Object, default: () => ({}) },
});

function count(items) {
	return items?.length || 0;
}
</script>

<template>
	<div class="widget-group">
		<div class="grid-col-2">
			<div class="widget border ul-scan-section">
				<div class="section-head">
					<span>{{ __("Client Scripts") }}</span>
					<span class="badge" :class="{ 'has-issues': count(conflicts.client_scripts) }">
						{{ count(conflicts.client_scripts) }}
					</span>
				</div>
				<ul v-if="conflicts.client_scripts?.length" class="ul-issue-list">
					<li
						v-for="hit in conflicts.client_scripts"
						:key="hit.name"
						:class="`issue-${hit.severity}`"
					>
						<strong>{{ hit.name }}</strong> · {{ hit.reference_doctype }}<br />
						<span class="text-muted">{{ hit.message }}</span>
					</li>
				</ul>
				<div v-else class="ul-empty">{{ __("No deprecated patterns detected") }}</div>
			</div>

			<div class="widget border ul-scan-section">
				<div class="section-head">
					<span>{{ __("Server Scripts") }}</span>
					<span class="badge" :class="{ 'has-issues': count(conflicts.server_scripts) }">
						{{ count(conflicts.server_scripts) }}
					</span>
				</div>
				<ul v-if="conflicts.server_scripts?.length" class="ul-issue-list">
					<li
						v-for="hit in conflicts.server_scripts"
						:key="hit.name"
						:class="`issue-${hit.severity}`"
					>
						<strong>{{ hit.name }}</strong> · {{ hit.reference_doctype }}<br />
						<span class="text-muted">{{ hit.message }}</span>
					</li>
				</ul>
				<div v-else class="ul-empty">{{ __("No deprecated patterns detected") }}</div>
			</div>

			<div class="widget border ul-scan-section">
				<div class="section-head">
					<span>{{ __("Custom App Hooks") }}</span>
					<span class="badge" :class="{ 'has-issues': count(conflicts.custom_apps_hooks) }">
						{{ count(conflicts.custom_apps_hooks) }}
					</span>
				</div>
				<ul v-if="conflicts.custom_apps_hooks?.length" class="ul-issue-list">
					<li v-for="hit in conflicts.custom_apps_hooks" :key="hit.app" class="issue-medium">
						<strong>{{ hit.app }}</strong>: {{ hit.unsupported_hooks.join(", ") }}
					</li>
				</ul>
				<div v-else class="ul-empty">{{ __("No unsupported hooks detected") }}</div>
			</div>

			<div class="widget border ul-scan-section">
				<div class="section-head">
					<span>{{ __("Schema Conflicts") }}</span>
					<span class="badge" :class="{ 'has-issues': count(conflicts.schema_conflicts) }">
						{{ count(conflicts.schema_conflicts) }}
					</span>
				</div>
				<ul v-if="conflicts.schema_conflicts?.length" class="ul-issue-list">
					<li v-for="hit in conflicts.schema_conflicts" :key="hit.custom_field" class="issue-high">
						{{ hit.message }}
					</li>
				</ul>
				<div v-else class="ul-empty">{{ __("No field name conflicts detected") }}</div>
			</div>

			<div class="widget border ul-scan-section full-width">
				<div class="section-head">
					<span>{{ __("Core App Modifications") }}</span>
					<span class="badge" :class="{ 'has-issues': count(conflicts.core_modifications) }">
						{{ count(conflicts.core_modifications) }}
					</span>
				</div>
				<ul v-if="conflicts.core_modifications?.length" class="ul-issue-list">
					<li
						v-for="report in conflicts.core_modifications"
						:key="report.app"
						:class="report.status === 'clean' ? '' : 'issue-high'"
					>
						<strong>{{ report.app }}</strong>
						<span class="indicator-pill no-indicator-dot filterable" :class="report.status === 'clean' ? 'green' : 'orange'">
							{{ report.status }}
						</span>
						· {{ report.modified_count || 0 }} {{ __("files") }}
						<ul v-if="report.modified_files?.length" class="margin-top text-small text-muted">
							<li v-for="file in report.modified_files.slice(0, 8)" :key="file.path">
								<code>{{ file.status }}</code> {{ file.path }}
							</li>
						</ul>
					</li>
				</ul>
				<div v-else class="ul-empty">{{ __("No modified core files detected") }}</div>
			</div>

			<div class="widget border ul-scan-section full-width">
				<div class="section-head">
					<span>{{ __("Installed Apps") }}</span>
					<span class="badge">{{ count(apps.apps) }}</span>
				</div>
				<table class="table table-bordered">
					<thead>
						<tr>
							<th>{{ __("App") }}</th>
							<th>{{ __("Version") }}</th>
							<th>{{ __("Type") }}</th>
							<th>{{ __("Git Status") }}</th>
						</tr>
					</thead>
					<tbody>
						<tr v-for="app in apps.apps || []" :key="app.app">
							<td><strong>{{ app.app }}</strong></td>
							<td>{{ app.version || "—" }}</td>
							<td>
								<span
									class="indicator-pill no-indicator-dot filterable"
									:class="app.is_official ? 'blue' : 'purple'"
								>
									{{ app.is_official ? __("Official") : __("Custom") }}
								</span>
							</td>
							<td>{{ app.git_report?.status || "—" }}</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
</template>

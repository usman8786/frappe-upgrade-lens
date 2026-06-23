import path from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
	plugins: [vue()],
	build: {
		outDir: path.resolve(__dirname, "../upgrade_lens/public/dist"),
		emptyOutDir: true,
		cssCodeSplit: false,
		rollupOptions: {
			input: path.resolve(__dirname, "src/main.js"),
			output: {
				format: "iife",
				name: "UpgradeLensDashboardModule",
				entryFileNames: "upgrade_lens_dashboard.js",
				assetFileNames: "style.css",
				inlineDynamicImports: true,
			},
		},
		target: "es2015",
	},
	define: {
		"process.env.NODE_ENV": JSON.stringify("production"),
	},
});

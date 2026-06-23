/** Frappe desk translation helper for Vue templates. */
export function __(text, ...args) {
	if (typeof window !== "undefined" && typeof window.__ === "function") {
		return window.__(text, ...args);
	}
	return text;
}

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        // Committed cinema grade — a single, intentional visual world.
        ink: {
          DEFAULT: "#0a0a0c", // near-black, faint cool slate bias
          2: "#101013", // lifted surface
          3: "#17171b", // card surface
        },
        paper: {
          DEFAULT: "#f3efe6", // warm off-white text
          dim: "#b6b1a7", // muted warm grey
          faint: "#7d7970", // faintest label grey
        },
        gold: {
          DEFAULT: "#c9a15a", // muted champagne brass (the accent)
          lift: "#e6c882", // brighter gold for small highlights
        },
        hair: {
          DEFAULT: "rgba(201,161,90,.20)", // warm hairline
          soft: "rgba(243,239,230,.09)", // neutral hairline
        },
      },
      fontFamily: {
        display: ['"Bodoni Moda"', '"Times New Roman"', "serif"],
        body: ['"Hanken Grotesk"', "system-ui", "-apple-system", "sans-serif"],
        mono: ['"JetBrains Mono"', "ui-monospace", '"SF Mono"', "monospace"],
      },
      fontSize: {
        // The fluid type scale, ported 1:1 from the original :root clamp()s.
        "step--1": "clamp(0.78rem, 0.75rem + 0.15vw, 0.86rem)",
        "step-0": "clamp(1rem, 0.96rem + 0.2vw, 1.12rem)",
        "step-1": "clamp(1.25rem, 1.15rem + 0.5vw, 1.6rem)",
        "step-2": "clamp(1.6rem, 1.4rem + 1vw, 2.4rem)",
        "step-3": "clamp(2.2rem, 1.7rem + 2.4vw, 3.8rem)",
        "step-4": "clamp(3.2rem, 2rem + 6vw, 8.5rem)",
      },
      maxWidth: {
        site: "1180px",
      },
      keyframes: {
        breathe: {
          "0%,100%": { opacity: ".82", transform: "translateY(0)" },
          "50%": { opacity: "1", transform: "translateY(-1.5%)" },
        },
        drop: {
          "0%,100%": { transform: "scaleY(.3)", opacity: ".4" },
          "50%": { transform: "scaleY(1)", opacity: "1" },
        },
        slide: {
          from: { transform: "translateX(0)" },
          to: { transform: "translateX(-50%)" },
        },
      },
      animation: {
        breathe: "breathe 26s ease-in-out infinite",
        drop: "drop 2.4s ease-in-out infinite",
        slide: "slide 46s linear infinite",
      },
    },
  },
  plugins: [],
};

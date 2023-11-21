/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./website/templates/*"],
  theme: {
    extend: {
      fontFamily: {
        custom: "'F1 Font', serif",
      },
      colors: {
        primary: "#e10500",
        secondary: "#15141f",
        background: "#f6f5f2",
      },
    },
  },
  plugins: [],
}


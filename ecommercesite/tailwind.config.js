/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', 
    './products/templates/**/*.html',
    './static/src/**/*.js',
    './cart/templates/**/*.html',

  ],
  theme: {
    extend: {},
  },
  variants: {
    fill: ['hover', 'focus'],
},
  plugins: [],
}

 
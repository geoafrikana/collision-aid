const toggleButton = document.getElementsByClassName('my-toggle-button')[0]
const navbarLinks = document.getElementsByClassName('my-navbar-links')[0]

toggleButton.addEventListener('click', () => {
  navbarLinks.classList.toggle('active')
})
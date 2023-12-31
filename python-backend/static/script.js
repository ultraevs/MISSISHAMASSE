let lastScroll = 0;
const defaultOffset = 100;
const header = document.querySelector('.header');

console.log(header.value)

const scrollPosition = () => window.pageYOffset || document.documentElement.scrollTop;
const containHide = () => header.classList.contains('back')


window.addEventListener('scroll', () => {
    if(scrollPosition() > lastScroll && !containHide() && scrollPosition() > defaultOffset){
        //scroll down
        header.classList.add('back');
    }
        else if (scrollPosition() < lastScroll && containHide() && scrollPosition() < defaultOffset){
        //scroll up
        header.classList.remove('back')
    }
    lastScroll = scrollPosition();
})

const anchors = document.querySelectorAll('a[href*="#"]')

for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()
    
    const blockID = anchor.getAttribute('href').substr(1)
    
    document.getElementById(blockID).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  })
}
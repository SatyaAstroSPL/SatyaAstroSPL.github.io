document.addEventListener('DOMContentLoaded', () => {
    // Highlight active link based on current URL
    const currentLocation = location.href;
    const menuItem = document.querySelectorAll('.nav-link');
    const menuLength = menuItem.length;
    for (let i = 0; i < menuLength; i++) {
        if (menuItem[i].href === currentLocation) {
            menuItem[i].className = "nav-link active";
        }
    }

    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('toggle');
        });
    }
    // Scroll Reveal Intersection Observer
    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // stop observing once it's revealed to keep it smooth
                observer.unobserve(entry.target);
            }
        });
    };

    const revealObserver = new IntersectionObserver(revealCallback, {
        threshold: 0.1
    });

    const revealElements = document.querySelectorAll('.reveal, .reveal-stagger');
    revealElements.forEach(el => revealObserver.observe(el));

    // Go Up Button Logic
    const goUpBtn = document.createElement('button');
    goUpBtn.className = 'go-up-btn';
    goUpBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    goUpBtn.setAttribute('aria-label', 'Go to top');
    document.body.appendChild(goUpBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            goUpBtn.classList.add('show');
        } else {
            goUpBtn.classList.remove('show');
        }
    });

    goUpBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

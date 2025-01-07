document.addEventListener('DOMContentLoaded', function () {
    // Initialize AOS
    AOS.init({
        duration: 1000,
        once: true
    });

    // Add hover sound effect
    const hoverSound = new Audio('/static/sounds/hover.mp3');
    hoverSound.preload = "auto"; // Preload the audio file

    document.querySelectorAll('.nav-link, .btn').forEach(element => {
        element.addEventListener('mouseenter', () => {
            hoverSound.currentTime = 0; // Restart audio from the beginning
            hoverSound.volume = 0.2;

            // Attempt to play the audio
            hoverSound.play().catch((error) => {
                console.warn('Audio playback failed:', error);
            });
        });
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Navbar background change on scroll
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            document.querySelector('.navbar').style.backgroundColor = '#1a1a1a';
        } else {
            document.querySelector('.navbar').style.backgroundColor = '#212529';
        }
    });
});

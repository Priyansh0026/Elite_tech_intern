// Theme Toggle & Interactive Controls - Priyansh Jain
document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');

    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
        if (theme === 'dark') {
            themeIcon.className = 'fa-solid fa-sun';
        } else {
            themeIcon.className = 'fa-solid fa-moon';
        }
    }

    // 2. Typing Effect for Hero Subtitle
    const typedTextSpan = document.getElementById('typed-text');
    const roles = [
        "Data Analyst & ML Enthusiast",
        "Sabudh Data Analytics Intern",
        "Elite Tech Data Science Intern",
        "Blinkit & Zomato Analytics",
        "IPL Capstone & Big Data Analyst"
    ];

    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingDelay = 100;
    let erasingDelay = 50;
    let newRoleDelay = 2000;

    function type() {
        if (!typedTextSpan) return;

        const currentRole = roles[roleIndex];

        if (isDeleting) {
            typedTextSpan.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
            typingDelay = erasingDelay;
        } else {
            typedTextSpan.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
            typingDelay = 100;
        }

        if (!isDeleting && charIndex === currentRole.length) {
            typingDelay = newRoleDelay;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            typingDelay = 500;
        }

        setTimeout(type, typingDelay);
    }

    if (roles.length) setTimeout(type, 500);

    // 3. Restore User's Saved Avatar & Position from localStorage (if any)
    const portfolioAvatar = document.querySelector('.avatar-img');
    if (portfolioAvatar) {
        const customSrc = localStorage.getItem('customAvatarSrc');
        const zoom = localStorage.getItem('avatarZoom');
        const posX = localStorage.getItem('avatarPosX');
        const posY = localStorage.getItem('avatarPosY');

        if (customSrc) {
            portfolioAvatar.src = customSrc;
        }
        if (zoom !== null || posX !== null || posY !== null) {
            const z = zoom || 1;
            const x = posX || 0;
            const y = posY || 0;
            portfolioAvatar.style.transform = `translate(${x}px, ${y}px) scale(${z})`;
        }
    }
});

// Global Contact Form Handler (Completely Prevents Outlook / Mailto Opening)
window.handleContactSubmit = function (e) {
    if (e) e.preventDefault();

    const contactForm = document.getElementById('contact-form');
    const submitBtn = document.getElementById('btn-submit-message');
    const toast = document.getElementById('toast-notification');

    if (!contactForm) return false;

    const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Send Message &rarr;';

    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';
    }

    const formData = new FormData(contactForm);
    const payload = {
        access_key: "77bdccd4-e741-47fa-9935-dd89b481e4ae",
        name: formData.get('name') || '',
        email: formData.get('email') || '',
        subject: formData.get('subject') || 'New Portfolio Contact Message',
        message: formData.get('message') || ''
    };

    fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
        contactForm.reset();
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnText;
        }
        showToastNotification();
    })
    .catch(err => {
        contactForm.reset();
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnText;
        }
        showToastNotification();
    });

    return false;
};

function showToastNotification() {
    const toast = document.getElementById('toast-notification');
    if (!toast) return;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 4000);
}

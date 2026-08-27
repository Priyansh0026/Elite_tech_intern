// Theme Toggle & Interactive Controls - Priyansh Jain (Juan James Theme)
document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Toggle (Dark / Light Theme)
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn ? themeToggleBtn.querySelector('i') : null;

    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        if (theme === 'dark') {
            themeIcon.className = 'fa-solid fa-sun';
        } else {
            themeIcon.className = 'fa-solid fa-moon';
        }
    }

    // 2. Active Nav Link on Scroll
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a[href]');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 150;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
});

// Global Contact Form Handler (Web3Forms API + Toast Notification)
window.handleContactSubmit = function (e) {
    if (e) e.preventDefault();

    const contactForm = document.getElementById('contact-form');
    const submitBtn = document.getElementById('btn-submit-message');

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

document.addEventListener('DOMContentLoaded', () => {
  // Universal hamburger toggle
  const hamburger = document.getElementById('hamburger');
  if (hamburger) {
    hamburger.setAttribute('role', 'button');
    hamburger.setAttribute('tabindex', '0');
    hamburger.setAttribute('aria-expanded', 'false');

    const toggleNav = () => {
      const nav = document.getElementById('mobileNav') || document.getElementById('nav-menu') || document.getElementById('navMobile') || document.querySelector('nav');
      if (!nav) return;

      if (nav.classList) {
        nav.classList.toggle('open');
        const isOpen = nav.classList.contains('open');
        hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        if (isOpen) {
          nav.style.setProperty('display', 'flex', 'important');
        } else {
          nav.style.removeProperty('display');
        }
      } else {
        nav.style.display = nav.style.display === 'flex' ? 'none' : 'flex';
      }
    };

    hamburger.addEventListener('click', toggleNav);
    hamburger.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleNav();
      }
    });

    // Close nav when a nav link is clicked (mobile)
    const nav = document.getElementById('mobileNav') || document.getElementById('nav-menu') || document.getElementById('navMobile') || document.querySelector('nav');
    if (nav) {
      nav.addEventListener('click', (e) => {
        const target = e.target;
        if (target && target.tagName === 'A') {
          if (nav.classList && nav.classList.contains('open')) {
            nav.classList.remove('open');
            hamburger.setAttribute('aria-expanded', 'false');
            nav.style.display = 'none';
          }
        }
      });
    }
  }

  // Back to top button
  const backToTop = document.getElementById('backToTop');
  if (backToTop) {
    const onScroll = () => {
      if (window.pageYOffset > 300) backToTop.classList.add('show'); else backToTop.classList.remove('show');
    };
    window.addEventListener('scroll', onScroll);
    onScroll();
    backToTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Smooth scrolling for anchor links with hashes
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href && href.startsWith('#')) {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });

  // Generic click handlers for buttons that navigate (ensure they exist)
  document.querySelectorAll('button[data-href]').forEach(btn => {
    btn.addEventListener('click', () => {
      const url = btn.getAttribute('data-href');
      if (url) window.location.href = url;
    });
  });

  // If a contact form exists but no handler, add a safe fallback
  const contactForm = document.getElementById('contactForm');
  if (contactForm && !contactForm.dataset.hasHandler) {
    contactForm.addEventListener('submit', function(e){
      e.preventDefault();
      const successMsg = document.getElementById('successMessage');
      if (successMsg) {
        successMsg.classList.add('show');
        this.reset();
        setTimeout(()=> successMsg.classList.remove('show'), 3000);
      }
    });
    contactForm.dataset.hasHandler = 'true';
  }
});

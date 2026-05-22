// Navbar scroll effect
window.addEventListener('scroll', () => {
  const nav = document.querySelector('.main-nav');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
});

// Counter animation
function animateCounters() {
  document.querySelectorAll('.count-up').forEach(el => {
    const target = parseInt(el.dataset.target || el.innerText);
    let current = 0;
    const step = Math.ceil(target / 60);
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.innerText = current + (el.dataset.suffix || '');
      if (current >= target) clearInterval(timer);
    }, 25);
  });
}

// Intersection observer for counters
const counterSection = document.querySelector('.stats-bar');
if (counterSection) {
  const obs = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) { animateCounters(); obs.disconnect(); }
  }, { threshold: 0.5 });
  obs.observe(counterSection);
}

// Gallery lightbox
document.querySelectorAll('.gallery-item').forEach(item => {
  item.addEventListener('click', () => {
    const src = item.querySelector('img')?.src;
    const cap = item.querySelector('.gallery-overlay span')?.innerText || '';
    if (!src) return;
    const modal = document.createElement('div');
    modal.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.92);z-index:9999;display:flex;align-items:center;justify-content:center;padding:20px;cursor:pointer;';
    modal.innerHTML = `<div style="max-width:90vw;max-height:90vh;text-align:center;">
      <img src="${src}" style="max-width:100%;max-height:80vh;border-radius:12px;box-shadow:0 20px 60px rgba(0,0,0,0.5);">
      ${cap ? `<p style="color:rgba(255,255,255,0.8);margin-top:12px;font-size:15px;">${cap}</p>` : ''}
      <p style="color:rgba(255,255,255,0.4);font-size:13px;margin-top:8px;">Click anywhere to close</p>
    </div>`;
    modal.addEventListener('click', () => modal.remove());
    document.body.appendChild(modal);
  });
});

// Smooth reveal on scroll
const revealEls = document.querySelectorAll('.card-course, .card-faculty, .notice-item, .card-founder');
const revObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity = '1';
      e.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });
revealEls.forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  revObs.observe(el);
});
      const slides = document.querySelectorAll("#schoolCarousel .slide");
      let currentSlide = 0;

      setInterval(() => {
        slides[currentSlide].classList.remove("opacity-100");
        slides[currentSlide].classList.add("opacity-0");

        currentSlide = (currentSlide + 1) % slides.length;

        slides[currentSlide].classList.remove("opacity-0");
        slides[currentSlide].classList.add("opacity-100");
      }, 4000);

      
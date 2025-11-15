// Filter functionality
        const filterButtons = document.querySelectorAll('.gallery-filter-btn');
        const galleryItems = document.querySelectorAll('.gallery-item');

        filterButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                
                // Add active class to clicked button
                this.classList.add('active');
                
                const filterValue = this.textContent.toLowerCase();
                
                // Filter gallery items
                galleryItems.forEach(item => {
                    const badge = item.querySelector('.gallery-category-badge');
                    const category = badge ? badge.textContent.toLowerCase() : '';
                    
                    if (filterValue === 'all' || category === filterValue) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
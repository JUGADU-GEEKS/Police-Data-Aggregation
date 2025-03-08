// Initialize Feather icons
document.addEventListener('DOMContentLoaded', function() {
    // Initialize feather icons
    feather.replace();
    
    // Set current year in footer
    document.getElementById('current-year').textContent = new Date().getFullYear();
    
    // Form elements
    const policeForm = document.getElementById('police-form');
    const formSection = document.getElementById('form-section');
    const successSection = document.getElementById('success-section');
    const resetButton = document.getElementById('reset-button');
    const submitButton = document.getElementById('submit-button');
    
    // Form inputs
    const stationIdInput = document.getElementById('stationId');
    const locationInput = document.getElementById('location');
    const officerInput = document.getElementById('officer');
    const phoneNumberInput = document.getElementById('phoneNumber');
    const emailInput = document.getElementById('email');
    const descriptionInput = document.getElementById('description');
    
    // Error elements
    const stationIdError = document.getElementById('stationId-error');
    const locationError = document.getElementById('location-error');
    const officerError = document.getElementById('officer-error');
    const phoneNumberError = document.getElementById('phoneNumber-error');
    const emailError = document.getElementById('email-error');
    
    // Form validation function
    function validateForm() {
      let isValid = true;
      
      // Reset all error states
      resetErrors();
      
      // Validate Station ID
      if (!stationIdInput.value.trim()) {
        showError(stationIdInput, stationIdError, 'Station ID is required');
        isValid = false;
      }
      
      // Validate Location
      if (!locationInput.value.trim()) {
        showError(locationInput, locationError, 'Location is required');
        isValid = false;
      }
      
      // Validate Officer Name
      if (!officerInput.value.trim()) {
        showError(officerInput, officerError, 'Officer name is required');
        isValid = false;
      }
      
      // Validate Phone Number
      if (!phoneNumberInput.value.trim()) {
        showError(phoneNumberInput, phoneNumberError, 'Phone number is required');
        isValid = false;
      } else if (!/^\d{10}$/.test(phoneNumberInput.value.replace(/\D/g, ''))) {
        showError(phoneNumberInput, phoneNumberError, 'Please enter a valid 10-digit phone number');
        isValid = false;
      }
      
      // Validate Email
      if (!emailInput.value.trim()) {
        showError(emailInput, emailError, 'Email is required');
        isValid = false;
      } else if (!/\S+@\S+\.\S+/.test(emailInput.value)) {
        showError(emailInput, emailError, 'Please enter a valid email address');
        isValid = false;
      }
      
      return isValid;
    }
    
    // Show error message
    function showError(inputElement, errorElement, message) {
      inputElement.classList.add('error');
      errorElement.classList.add('show');
      errorElement.querySelector('span').textContent = message;
    }
    
    // Reset all error states
    function resetErrors() {
      const inputs = [stationIdInput, locationInput, officerInput, phoneNumberInput, emailInput];
      const errors = [stationIdError, locationError, officerError, phoneNumberError, emailError];
      
      inputs.forEach(input => input.classList.remove('error'));
      errors.forEach(error => {
        error.classList.remove('show');
        error.querySelector('span').textContent = '';
      });
    }
    
    // Handle input changes (clear errors on change)
    const allInputs = [stationIdInput, locationInput, officerInput, phoneNumberInput, emailInput, descriptionInput];
    allInputs.forEach(input => {
      input.addEventListener('input', function() {
        this.classList.remove('error');
        const id = this.id;
        const errorElement = document.getElementById(`${id}-error`);
        if (errorElement) {
          errorElement.classList.remove('show');
        }
      });
    });
    
    // Form submission
    policeForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      if (!validateForm()) {
        return;
      }
      
      // Show submitting state
      submitButton.disabled = true;
      submitButton.textContent = 'Submitting...';
      
      // Simulate API call
      setTimeout(() => {
        // Get form data
        const formData = {
          stationId: stationIdInput.value,
          location: locationInput.value,
          officer: officerInput.value,
          phoneNumber: phoneNumberInput.value,
          email: emailInput.value,
          description: descriptionInput.value
        };
        
        // Log form data (in a real app, this would be sent to a server)
        console.log('Form data submitted:', formData);
        
        // Show success message
        formSection.classList.add('hide');
        successSection.classList.remove('hide');
        
        // Reset form for future submissions
        policeForm.reset();
        submitButton.disabled = false;
        submitButton.textContent = 'Submit Information';
      }, 1500);
    });
    
    // Reset button action
    resetButton.addEventListener('click', function() {
      successSection.classList.add('hide');
      formSection.classList.remove('hide');
    });
  });
  
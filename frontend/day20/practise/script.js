
const form = document.getElementById('registrationForm');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    const inp1 = document.getElementById('inp1');
    const inp2 = document.getElementById('inp2');
    const inp3 = document.getElementById('inp3');
    const inp4 = document.getElementById('inp4');
    const inp5 = document.getElementById('inp5');

    const error1 = document.getElementById('error1');
    const error2 = document.getElementById('error2');
    const error3 = document.getElementById('error3');
    const error4 = document.getElementById('error4');
    const error5 = document.getElementById('error5');
    const error6 = document.getElementById('error6');
    const error7 = document.getElementById('error7');

    const success = document.getElementById('success');

    // Reset previous messages and borders
    const inputs = [inp1, inp2, inp3, inp4, inp5];

    inputs.forEach(input => {
        input.style.border = '1px solid #cbd5e1';
    });

    document.querySelectorAll('.error').forEach(error => {
        error.textContent = '';
    });

    success.textContent = '';

    let isValid = true;

    function showError(input, errorElement, message) {
        errorElement.textContent = message;
        input.style.border = '2px solid red';
        isValid = false;
    }

    function showSuccess(input) {
        input.style.border = '2px solid green';
    }

    // 1. Validate name
    if (inp1.value.trim() === '') {
        showError(inp1, error1, 'Please enter your name.');
    } else {
        showSuccess(inp1);
    }

    // 2. Validate email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (inp2.value.trim() === '') {
        showError(inp2, error2, 'Please enter your email.');
    } else if (!emailPattern.test(inp2.value.trim())) {
        showError(inp2, error2, 'Please enter a valid email.');
    } else {
        showSuccess(inp2);
    }

    // 3. Validate password
    if (inp3.value.length < 8) {
        showError(inp3, error3, 'Password must be at least 8 characters.');
    } else {
        showSuccess(inp3);
    }

    // 4. Validate confirm password
    if (inp4.value === '') {
        showError(inp4, error4, 'Please confirm your password.');
    } else if (inp4.value !== inp3.value) {
        showError(inp4, error4, 'Passwords do not match.');
    } else {
        showSuccess(inp4);
    }

    // 5. Validate age
    const age = Number(inp5.value);

    if (inp5.value.trim() === '') {
        showError(inp5, error5, 'Please enter your age.');
    } else if (!Number.isInteger(age) || age < 18 || age > 100) {
        showError(inp5, error5, 'Age must be a whole number from 18 to 100.');
    } else {
        showSuccess(inp5);
    }

    // 6. Validate gender
    const selectedGender = document.querySelector(
        'input[name="gender"]:checked'
    );

    if (!selectedGender) {
        error6.textContent = 'Please select your gender.';
        isValid = false;
    }

    // 7. Validate terms
    const terms = document.getElementById('terms');

    if (!terms.checked) {
        error7.textContent = 'Please accept the terms and conditions.';
        isValid = false;
    }

    // Final result
    if (isValid) {
        success.textContent = 'All validations passed!';
    }
});

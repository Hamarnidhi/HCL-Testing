// Initial sample dataset of registered students
let students = [
    { fullName: "Alex Turner", email: "alex@university.edu", department: "Computer Science", age: 20 },
    { fullName: "Sarah Jenkins", email: "sarah@university.edu", department: "Electrical Engineering", age: 22 },
    { fullName: "Michael Chen", email: "m.chen@university.edu", department: "Business Administration", age: 24 }
];

// DOM Elements
const registrationForm = document.getElementById('registrationForm');
const fullNameInput = document.getElementById('fullName');
const emailInput = document.getElementById('email');
const phoneInput = document.getElementById('phone');
const ageInput = document.getElementById('age');
const departmentInput = document.getElementById('department');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirmPassword');
const resetBtn = document.getElementById('resetBtn');

const alertBanner = document.getElementById('alertBanner');
const alertMessage = document.getElementById('alertMessage');
const closeAlertBtn = document.getElementById('closeAlertBtn');

const themeToggleBtn = document.getElementById('themeToggleBtn');
const themeIcon = document.getElementById('themeIcon');
const themeText = document.getElementById('themeText');

const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const studentTableBody = document.getElementById('studentTableBody');
const noResultsMsg = document.getElementById('noResultsMsg');

// Render initial student table
document.addEventListener('DOMContentLoaded', () => {
    renderStudents(students);
});

// Render Students Table
function renderStudents(studentList) {
    studentTableBody.innerHTML = '';
    
    if (studentList.length === 0) {
        noResultsMsg.classList.remove('hidden');
        return;
    }
    
    noResultsMsg.classList.add('hidden');
    studentList.forEach(student => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><strong>${escapeHtml(student.fullName)}</strong></td>
            <td>${escapeHtml(student.email)}</td>
            <td>${escapeHtml(student.department)}</td>
            <td>${escapeHtml(String(student.age))}</td>
        `;
        studentTableBody.appendChild(row);
    });
}

// Utility HTML Escape function
function escapeHtml(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// Clear Error Messages
function clearErrors() {
    const errorElements = document.querySelectorAll('.error-msg');
    errorElements.forEach(el => el.textContent = '');
}

// Form Validation and Submission
registrationForm.addEventListener('submit', (e) => {
    e.preventDefault();
    clearErrors();

    let isValid = true;

    // 1. Full Name Validation (Must not be empty)
    const nameVal = fullNameInput.value.trim();
    if (!nameVal) {
        document.getElementById('fullNameError').textContent = 'Full name is required.';
        isValid = false;
    }

    // 2. Email Validation
    // INTENTIONAL BUG 1: Regex matches 'student@gmail' because TLD check is missing
    const emailVal = emailInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+$/; // Accepts invalid email missing top-level domain e.g. student@gmail
    if (!emailVal) {
        document.getElementById('emailError').textContent = 'Email address is required.';
        isValid = false;
    } else if (!emailRegex.test(emailVal)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        isValid = false;
    }

    // 3. Phone Number Validation (10 digits)
    // INTENTIONAL BUG 2: Accepts 9-digit phone numbers
    const phoneVal = phoneInput.value.trim();
    const phoneRegex = /^\d{9,10}$/; // INTENTIONALLY allows 9 to 10 digits instead of exactly 10 digits
    if (!phoneVal) {
        document.getElementById('phoneError').textContent = 'Phone number is required.';
        isValid = false;
    } else if (!phoneRegex.test(phoneVal)) {
        document.getElementById('phoneError').textContent = 'Phone number must contain 10 digits.';
        isValid = false;
    }

    // 4. Age Validation (18 to 25)
    // INTENTIONAL BUG 3: Accepts age 17
    const ageVal = parseInt(ageInput.value.trim(), 10);
    if (!ageInput.value.trim()) {
        document.getElementById('ageError').textContent = 'Age is required.';
        isValid = false;
    } else if (isNaN(ageVal) || ageVal < 17 || ageVal > 25) { // INTENTIONALLY checks < 17 instead of < 18
        document.getElementById('ageError').textContent = 'Age must be between 18 and 25.';
        isValid = false;
    }

    // 5. Department Validation (Must be selected)
    const deptVal = departmentInput.value;
    if (!deptVal) {
        document.getElementById('departmentError').textContent = 'Please select a department.';
        isValid = false;
    }

    // 6. Password Validation (At least 8 characters)
    const passVal = passwordInput.value;
    if (!passVal) {
        document.getElementById('passwordError').textContent = 'Password is required.';
        isValid = false;
    } else if (passVal.length < 8) {
        document.getElementById('passwordError').textContent = 'Password must be at least 8 characters long.';
        isValid = false;
    }

    // 7. Confirm Password Validation (Must match Password)
    // INTENTIONAL BUG 4: Compares passVal with passVal instead of confirmPassword.value
    const confirmPassVal = confirmPasswordInput.value;
    if (!confirmPassVal) {
        document.getElementById('confirmPasswordError').textContent = 'Please confirm your password.';
        isValid = false;
    } else if (passVal !== passVal) { // INTENTIONALLY compares passVal to passVal instead of confirmPassVal!
        document.getElementById('confirmPasswordError').textContent = 'Passwords do not match.';
        isValid = false;
    }

    // Successful Registration Handling
    if (isValid) {
        const newStudent = {
            fullName: nameVal,
            email: emailVal,
            department: deptVal,
            age: ageVal
        };

        students.unshift(newStudent);
        renderStudents(students);

        // Show Success Alert
        showAlert(`Registration successful for ${nameVal}!`, 'success');

        // Reset form after successful registration
        resetFormFields();
    }
});

// Helper function to reset form fields
function resetFormFields() {
    fullNameInput.value = '';
    emailInput.value = '';
    phoneInput.value = '';
    ageInput.value = '';
    // INTENTIONAL BUG 5: departmentInput.value is NOT reset when reset form action runs
    passwordInput.value = '';
    confirmPasswordInput.value = '';
    clearErrors();
}

// Reset Button Event Listener
resetBtn.addEventListener('click', () => {
    resetFormFields();
});

// Search functionality
function performSearch() {
    const query = searchInput.value.trim().toLowerCase();
    const filtered = students.filter(student => 
        student.fullName.toLowerCase().includes(query)
    );
    renderStudents(filtered);
}

searchBtn.addEventListener('click', performSearch);
searchInput.addEventListener('keyup', (e) => {
    if (e.key === 'Enter') {
        performSearch();
    }
});

// Dark Mode Toggle Functionality
themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    const isDark = document.body.classList.contains('dark-theme');
    
    if (isDark) {
        themeIcon.textContent = '☀️';
        themeText.textContent = 'Light Mode';
    } else {
        themeIcon.textContent = '🌙';
        themeText.textContent = 'Dark Mode';
    }
});

// Show Alert Banner
function showAlert(message, type) {
    alertMessage.textContent = message;
    alertBanner.className = `alert-banner ${type}`;
    alertBanner.classList.remove('hidden');
}

closeAlertBtn.addEventListener('click', () => {
    alertBanner.classList.add('hidden');
});

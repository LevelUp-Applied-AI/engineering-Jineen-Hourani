# SQL Query Results — Day 8

## Query 1: All Students (ordered by prereq_score DESC)

(6, 'Lina Barakat', '2024B', 'Jordan', 95.0)
(12, 'Sara Mahmoud', '2025A', 'Jordan', 93.5)
(1, 'Aisha Al-Rashidi', '2024A', 'Jordan', 91.0)
(10, 'Dina Saleh', '2024B', 'Egypt', 89.0)
(5, 'Tariq Farouk', '2024A', 'Palestine', 88.5)
(3, 'Nour Mansour', '2024A', 'Jordan', 84.0)
(14, 'Maya Qassem', '2025A', 'Palestine', 82.0)
(8, 'Rania Odeh', '2024B', 'Jordan', 80.0)
(2, 'Omar Khalil', '2024A', 'Jordan', 78.5)
(11, 'Faris Awad', '2025A', 'Jordan', 77.0)
(7, 'Sami Nabulsi', '2024B', 'Palestine', 72.0)
(15, 'Hamza Tawfiq', '2025A', 'Jordan', 70.0)
(4, 'Yasmin Haddad', '2024A', 'Jordan', 67.0)
(9, 'Khalil Jaber', '2024B', 'Jordan', 61.5)
(13, 'Yousef Al-Ahmad', '2025A', 'Jordan', 55.0)

---

## Query 2: Students with prereq_score >= 80

('Lina Barakat', 'Jordan', 95.0)
('Sara Mahmoud', 'Jordan', 93.5)
('Aisha Al-Rashidi', 'Jordan', 91.0)
('Dina Saleh', 'Egypt', 89.0)
('Tariq Farouk', 'Palestine', 88.5)
('Nour Mansour', 'Jordan', 84.0)
('Maya Qassem', 'Palestine', 82.0)
('Rania Odeh', 'Jordan', 80.0)

---

## Query 3: Average Score by Cohort

('2024A', 5, 81.8)
('2024B', 5, 79.5)
('2025A', 5, 75.5)

---

## Query 4: Students + Projects (non-missing)

('Aisha Al-Rashidi', '2024A', 'Laptop Verify', 1, 'submitted', 95.0)
('Aisha Al-Rashidi', '2024A', 'Python Env', 2, 'submitted', 88.0)
('Aisha Al-Rashidi', '2024A', 'PR Hygiene', 3, 'submitted', 92.0)
('Dina Saleh', '2024B', 'Laptop Verify', 1, 'submitted', 90.0)
('Dina Saleh', '2024B', 'Python Env', 2, 'submitted', 88.0)
('Faris Awad', '2025A', 'Laptop Verify', 1, 'submitted', 77.0)
('Hamza Tawfiq', '2025A', 'Laptop Verify', 1, 'submitted', 72.0)
('Hamza Tawfiq', '2025A', 'Python Env', 2, 'late', 65.0)
('Lina Barakat', '2024B', 'Laptop Verify', 1, 'submitted', 98.0)
('Lina Barakat', '2024B', 'Python Env', 2, 'submitted', 95.0)
('Lina Barakat', '2024B', 'PR Hygiene', 3, 'submitted', 96.0)
('Maya Qassem', '2025A', 'Laptop Verify', 1, 'submitted', 84.0)
('Nour Mansour', '2024A', 'Laptop Verify', 1, 'submitted', 85.0)
('Nour Mansour', '2024A', 'Python Env', 2, 'submitted', 90.0)
('Nour Mansour', '2024A', 'PR Hygiene', 3, 'submitted', 87.0)
('Omar Khalil', '2024A', 'Laptop Verify', 1, 'submitted', 80.0)
('Omar Khalil', '2024A', 'Python Env', 2, 'late', 72.0)
('Rania Odeh', '2024B', 'Laptop Verify', 1, 'submitted', 82.0)
('Rania Odeh', '2024B', 'Python Env', 2, 'submitted', 79.0)
('Sami Nabulsi', '2024B', 'Laptop Verify', 1, 'submitted', 74.0)
('Sami Nabulsi', '2024B', 'Python Env', 2, 'late', 68.0)
('Sara Mahmoud', '2025A', 'Laptop Verify', 1, 'submitted', 94.0)
('Sara Mahmoud', '2025A', 'Python Env', 2, 'submitted', 91.0)
('Tariq Farouk', '2024A', 'Laptop Verify', 1, 'submitted', 91.0)
('Tariq Farouk', '2024A', 'Python Env', 2, 'submitted', 86.0)
('Yasmin Haddad', '2024A', 'Laptop Verify', 1, 'late', 65.0)
('Yousef Al-Ahmad', '2025A', 'Laptop Verify', 1, 'late', 52.0)

---

# Interpretation

**Question 1:** Which cohort had the highest average pre-work score? What might that tell you about how cohorts differ?

The 2024A cohort had the highest average pre-work score (81.8). This may suggest that students in this cohort performed slightly better in the pre-work compared to the other cohorts.

**Question 2:** Looking at Query 2 results: how many students scored 80 or above? Does anything about their countries surprise you?

Eight students scored 80 or above. Most of them are from Jordan, with a few from Palestine and Egypt, showing that strong performance appears across multiple countries.

**Question 3:** From the JOIN results (Query 4): choose one student and describe their project submission pattern. What does the data tell you about this learner?

Lina Barakat consistently submitted all projects and achieved very high grades (98, 95, and 96). This suggests that she is a highly consistent and high-performing student.
% ====================================================================
% Aim: To write a Prolog program to query relationships between 
%      students, teachers, and subjects.
% ====================================================================

% Step 1: Define teaches/2 facts linking teachers to their subjects.
% Format: teaches(TeacherName, SubjectCode).
teaches(dr_smith, csa17).
teaches(prof_jones, cs102).
teaches(dr_davis, mat301).
teaches(ms_taylor, eng101).

% Step 2: Define takes/2 facts linking students to subjects they study.
% Format: takes(StudentName, SubjectCode).
takes(rahul, csa17).
takes(rahul, mat301).
takes(priya, csa17).
takes(priya, eng101).
takes(amit, cs102).
takes(amit, mat301).

% Step 3: Define teaching_subjects/2 and taking_students/2 predicates.
% teaching_subjects/2 looks up what subject code a specific teacher instructs.
teaching_subjects(Teacher, SubjectCode) :-
    teaches(Teacher, SubjectCode).

% taking_students/2 looks up what students are enrolled in a specific subject code.
taking_students(SubjectCode, Student) :-
    takes(Student, SubjectCode).

% ====================================================================
% Step 4: Query to find subjects by teacher or students by subject.
% ====================================================================
% To test this database, type the following queries into your Prolog interpreter:
%
% Query A: Find all subjects taught by 'dr_smith'
% ?- teaching_subjects(dr_smith, Subject).
% Output: Subject = csa17.
%
% Query B: Find all students taking the subject 'csa17'
% ?- taking_students(csa17, Student).
% Output: 
% Student = rahul ;
% Student = priya.
%
% Query C: Advanced relational query: Find which teacher teaches a specific student (e.g., rahul)
% ?- teaches(Teacher, Subject), takes(rahul, Subject).
% Output:
% Teacher = dr_smith, Subject = csa17 ;
% Teacher = dr_davis, Subject = mat301.
% ====================================================================

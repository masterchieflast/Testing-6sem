package ErrorExceptions;


import java.util.List;

public class Main {
    public static void main(String[] args) {
        University university = new University("Мой Университет");

        Faculty faculty = new Faculty("Факультет информационных технологий");

        Group group = new Group("Группа 101");

        Student student1 = new Student("Иванов");
        student1.addSubject(new Subject("Математика", 8.5));
        student1.addSubject(new Subject("Программирование", 9.0));
        group.addStudent(student1);

        Student student2 = new Student("Петров");
        student2.addSubject(new Subject("Математика", 7.0));
        student2.addSubject(new Subject("Программирование", 8.0));
        group.addStudent(student2);

        faculty.addGroup(group);

        university.addFaculty(faculty);

        double averageScore = calculateAverageScore(student1);
        System.out.println("Средний балл студента " + student1.getName() + ": " + averageScore);

        double averageSubjectScore = calculateAverageSubjectScore(university, "Факультет информационных технологий", "Группа 101", "Программирование");
        System.out.println("Средний балл по предмету Программирование на факультете: " + averageSubjectScore);

        double averageUniversityScore = calculateAverageUniversityScore(university, "Математика");
        System.out.println("Средний балл по предмету Математика в университете: " + averageUniversityScore);
    }

    /**
     * Метод для вычисления среднего балла студента по всем предметам
     */
    public static double calculateAverageScore(Student student) {
        List<Subject> subjects = student.getSubjects();
        if (subjects.isEmpty()) {
            throw new IllegalArgumentException("Отсутствуют предметы у студента");
        }
        double totalScore = 0;
        for (Subject subject : subjects) {
            totalScore += subject.getScore();
        }
        return totalScore / subjects.size();
    }

    /**
     * Метод для вычисления среднего балла по конкретному предмету в конкретной группе и на конкретном факультете
     */
    public static double calculateAverageSubjectScore(University university, String facultyName, String groupName, String subjectName) {
        Faculty faculty = university.getFaculties().get(facultyName);
        if (faculty == null) {
            throw new IllegalArgumentException("Факультет не найден");
        }
        Group group = faculty.getGroups().get(groupName);
        if (group == null) {
            throw new IllegalArgumentException("Группа не найдена");
        }
        List<Student> students = group.getStudents();
        if (students.isEmpty()) {
            throw new IllegalArgumentException("Отсутствуют студенты в группе");
        }
        double totalScore = 0;
        int count = 0;
        for (Student student : students) {
            for (Subject subject : student.getSubjects()) {
                if (subject.getName().equals(subjectName)) {
                    totalScore += subject.getScore();
                    count++;
                }
            }
        }
        if (count == 0) {
            throw new IllegalArgumentException("Отсутствует предмет " + subjectName + " в группе");
        }
        return totalScore / count;
    }

    /**
     * Метод для вычисления среднего балла по предмету для всего университета
     * Adware
     */
    public static double calculateAverageUniversityScore(University university, String subjectName) {
        double totalScore = 0;
        int count = 0;
        for (Faculty faculty : university.getFaculties().values()) {
            for (Group group : faculty.getGroups().values()) {
                for (Student student : group.getStudents()) {
                    for (Subject subject : student.getSubjects()) {
                        if (subject.getName().equals(subjectName)) {
                            totalScore += subject.getScore();
                            count++;
                        }
                    }
                }
            }
        }
        if (count == 0) {
            throw new IllegalArgumentException("Отсутствует предмет " + subjectName + " в университете");
        }
        return totalScore / count;
    }
}
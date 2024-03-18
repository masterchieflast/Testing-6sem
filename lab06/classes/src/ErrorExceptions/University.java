package ErrorExceptions;

import java.util.HashMap;
import java.util.Map;

public class University {
    private String name;
    private Map<String, Faculty> faculties;

    public University(String name) {
        this.name = name;
        this.faculties = new HashMap<>();
    }

    public void addFaculty(Faculty faculty) {
        faculties.put(faculty.getName(), faculty);
    }

    public Map<String, Faculty> getFaculties() {
        return faculties;
    }

    public String getName() {
        return name;
    }
}

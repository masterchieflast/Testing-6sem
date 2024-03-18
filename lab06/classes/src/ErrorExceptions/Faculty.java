package ErrorExceptions;

import java.util.HashMap;
import java.util.Map;

public class Faculty {private String name;
    private Map<String, Group> groups;

    public Faculty(String name) {
        this.name = name;
        this.groups = new HashMap<>();
    }

    public void addGroup(Group group) {
        groups.put(group.getName(), group);
    }

    public Map<String, Group> getGroups() {
        return groups;
    }

    public String getName() {
        return name;
    }
}

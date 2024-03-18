package ErrorExceptions;

public class Subject {
    private String name;
    private double score;

    public Subject(String name, double score) {
        this.name = name;
        if (score < 0 || score > 10) {
            throw new IllegalArgumentException("Оценка должна быть от 0 до 10");
        }
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public double getScore() {
        return score;
    }
}

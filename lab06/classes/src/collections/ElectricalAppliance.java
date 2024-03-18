package collections;

public abstract class ElectricalAppliance {
    protected String name;
    protected int power;

    public ElectricalAppliance(String name, int power) {
        this.name = name;
        this.power = power;
    }

    public int getPower() {
        return power;
    }

    public String getName() {
        return name;
    }
}

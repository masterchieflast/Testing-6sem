package collections;

import java.util.ArrayList;
import java.util.List;

public class ApplianceManager {
    private List<ElectricalAppliance> appliances;

    public ApplianceManager() {
        this.appliances = new ArrayList<>();
    }

    public void plugIn(ElectricalAppliance appliance) {
        appliances.add(appliance);
        System.out.println(appliance.getName() + " plugged in.");
    }

    public int calculateTotalPower() {
        int totalPower = 0;
        for (ElectricalAppliance appliance : appliances) {
            totalPower += appliance.getPower();
        }
        return totalPower;
    }

    public void sortByPower() {
        appliances.sort((a1, a2) -> Integer.compare(a1.getPower(), a2.getPower()));
    }

    public ElectricalAppliance findApplianceByPowerRange(int minPower, int maxPower) {
        for (ElectricalAppliance appliance : appliances) {
            int power = appliance.getPower();
            if (power >= minPower && power <= maxPower) {
                return appliance;
            }
        }
        return null;
    }
}

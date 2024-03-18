package Classes;

class Patien {
    private int id;
    private String lastName;
    private String firstName;
    private String middleName;
    private String address;
    private String phoneNumber;
    private int medicalCardNumber;
    private String diagnosis;

    // Constructors
    public Patien(int id, String lastName, String firstName, String middleName, String address, String phoneNumber, int medicalCardNumber, String diagnosis) {
        this.id = id;
        this.lastName = lastName;
        this.firstName = firstName;
        this.middleName = middleName;
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.medicalCardNumber = medicalCardNumber;
        this.diagnosis = diagnosis;
    }

    // Getters and Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getMiddleName() {
        return middleName;
    }

    public void setMiddleName(String middleName) {
        this.middleName = middleName;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public int getMedicalCardNumber() {
        return medicalCardNumber;
    }

    public void setMedicalCardNumber(int medicalCardNumber) {
        this.medicalCardNumber = medicalCardNumber;
    }

    public String getDiagnosis() {
        return diagnosis;
    }

    public void setDiagnosis(String diagnosis) {
        this.diagnosis = diagnosis;
    }

    // toString() method
    @Override
    public String toString() {
        return "Patient{" +
                "id=" + id +
                ", lastName='" + lastName + '\'' +
                ", firstName='" + firstName + '\'' +
                ", middleName='" + middleName + '\'' +
                ", address='" + address + '\'' +
                ", phoneNumber='" + phoneNumber + '\'' +
                ", medicalCardNumber=" + medicalCardNumber +
                ", diagnosis='" + diagnosis + '\'' +
                '}';
    }
}
using AirCompany;
using AirCompany.Models;
using AirCompany.Planes;
using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;

namespace AirCompanyTests.Tests
{
    [TestFixture]
    public class AirportTest
    {
        private readonly List<Plane> _planes = new List<Plane>(){
           new PassengerPlane("Boeing-737", 900, 12000, 60500, 164),
           new PassengerPlane("Boeing-737-800", 940, 12300, 63870, 192),
           new PassengerPlane("Boeing-747", 980, 16100, 70500, 242),
           new PassengerPlane("Airbus A320", 930, 11800, 65500, 188),
           new PassengerPlane("Airbus A330", 990, 14800, 80500, 222),
           new PassengerPlane("Embraer 190", 870, 8100, 30800, 64),
           new PassengerPlane("Sukhoi Superjet 100", 870, 11500, 50500, 140),
           new PassengerPlane("Bombardier CS300", 920, 11000, 60700, 196),
           new MilitaryPlane("B-1B Lancer", 1050, 21000, 80000, MilitaryType.BOMBER),
           new MilitaryPlane("B-2 Spirit", 1030, 22000, 70000, MilitaryType.BOMBER),
           new MilitaryPlane("B-52 Stratofortress", 1000, 20000, 80000, MilitaryType.BOMBER),
           new MilitaryPlane("F-15", 1500, 12000, 10000, MilitaryType.FIGHTER),
           new MilitaryPlane("F-22", 1550, 13000, 11000, MilitaryType.FIGHTER),
           new MilitaryPlane("C-130 Hercules", 650, 5000, 110000, MilitaryType.TRANSPORT)
   };

        private PassengerPlane _planeWithMaxPassengerCapacity = new PassengerPlane("Boeing-747", 980, 16100, 70500, 242);

        [Test]
        public void MyTest1()
        {
            var airport = new Airport(_planes);
            var transportMilitaryPlanes = airport.GetTransportMilitaryPlanes().ToList();
            var hasMilitaryTransportPlane = transportMilitaryPlanes.Any();

            Assert.IsTrue(hasMilitaryTransportPlane);
        }

        [Test]
        public void MyTest2()
        {
            var airport = new Airport(_planes);
            var expectedPlaneWithMaxPassengersCapacity = airport.GetPassengerPlaneWithMaxPassengersCapacity();
            Assert.AreEqual(_planeWithMaxPassengerCapacity, expectedPlaneWithMaxPassengersCapacity);
        }

        [Test]
        public void MyTest3()
        {
            var airport = new Airport(_planes);
            airport = airport.SortByMaxLoadCapacity();
            var planesSortedByMaxLoadCapacity = airport.GetPlanes().ToList();

            var nextPlaneMaxLoadCapacityIsHigherThanCurrent = true;
            for (var i = 0; i < planesSortedByMaxLoadCapacity.Count - 1; i++)
            {
                var currentPlane = planesSortedByMaxLoadCapacity[i];
                var nextPlane = planesSortedByMaxLoadCapacity[i + 1];
                if (currentPlane.MAXLoadCapacity() <= nextPlane.MAXLoadCapacity()) continue;
                nextPlaneMaxLoadCapacityIsHigherThanCurrent = false;
                break; // No need to continue checking if condition fails once
            }
            Assert.IsTrue(nextPlaneMaxLoadCapacityIsHigherThanCurrent);
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using AirCompany.Models;
using AirCompany.Planes;

namespace AirCompany
{
    public class Airport
    {
        private readonly List<Plane> _planes;

        public Airport(IEnumerable<Plane> planes)
        {
            _planes = planes.ToList();
        }

        public IEnumerable<PassengerPlane> GetPassengersPlanes()
        {
            return _planes.Where(t => t.GetType() == typeof(PassengerPlane)).Cast<PassengerPlane>().ToList();
        }

        public IEnumerable<MilitaryPlane> GetMilitaryPlanes()
        {
            return _planes.Where(t => t.GetType() == typeof(MilitaryPlane)).Cast<MilitaryPlane>().ToList();
        }

        public PassengerPlane GetPassengerPlaneWithMaxPassengersCapacity()
        {
            var passengerPlanes = GetPassengersPlanes();
            return passengerPlanes.Aggregate((w, x) 
                => w.PassengersCapacityIs() > x.PassengersCapacityIs() ? w : x);             
        }

        public IEnumerable<MilitaryPlane> GetTransportMilitaryPlanes()
        {
            var militaryPlanes = GetMilitaryPlanes();

            return militaryPlanes.Where(plane => plane.PlaneTypeIs() == MilitaryType.TRANSPORT).ToList();
        }

        public Airport SortByMaxDistance()
        {
            return new Airport(_planes.OrderBy(w => w.MAXFlightDistance()));
        }

        public Airport SortByMaxSpeed()
        {
            return new Airport(_planes.OrderBy(w => w.GetMS()));
        }

        public Airport SortByMaxLoadCapacity()
        {
            return new Airport(_planes.OrderBy(w => w.MAXLoadCapacity()));
        }


        public IEnumerable<Plane> GetPlanes() => _planes;

        public override string ToString()
        {
            return $"Airport{{planes=[{string.Join(", ", _planes.Select(x => x.GetModel()))}]}}";
        }
    }
}

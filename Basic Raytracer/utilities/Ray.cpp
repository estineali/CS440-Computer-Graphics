#include "Ray.hpp"

Ray::Ray()
{
	o = Point3D();
	d = Vector3D();
	w = 1;
}

Ray::Ray(const Point3D& origin, const Vector3D& dir)
{
	o = origin;
	d = dir; 
	w = 1;
}

std::string Ray::to_string() const
{
	std::string retval = "";
	retval.append(o.to_string() + ", ");
	retval.append(d.to_string() + ", ");
	retval.append(std::to_string(w) + ")");

	return retval;
}


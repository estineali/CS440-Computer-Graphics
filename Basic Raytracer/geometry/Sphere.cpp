#include "Sphere.hpp"
#include "../utilities/BBox.hpp"


Sphere::Sphere()
{
	c = Point3D(0);
	r = 0.0f;
}

Sphere::Sphere(const Point3D& center, float radius)
{
	c = center;
	r = radius;
}

Sphere::Sphere(const Sphere& object)
{
	c = object.c;
	r = object.r;
}

Sphere& Sphere::operator=(const Sphere& rhs)
{
	c = rhs.c;
	r = rhs.r; 

	return *this; 
}

std::string Sphere::to_string() const
{
	std::string retval = "(" + c.to_string() + ", " + std::to_string(r) + ")"; 
	return retval;
}

BBox Sphere::getBBox() const
{
	Point3D P0 = Point3D(c.x - r, c.y - r, c.z - r);
	Point3D P1 = Point3D(c.x + r, c.y + r, c.z + r);

	return BBox(P0, P1);
}


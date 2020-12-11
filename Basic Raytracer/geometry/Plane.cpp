#include "Plane.hpp"
#include "../utilities/Ray.hpp"
#include "../utilities/ShadeInfo.hpp"
#include "../utilities/BBox.hpp"

Plane::Plane()
{
	a = Point3D();
	n = Vector3D(0, 1, 0); 
}

Plane::Plane(const Point3D& pt, const Vector3D& n)
{
	a = pt; 
	this->n = n;
	this->n.normalize();
}

Plane::Plane(const Plane& object)
{
	a = object.a;
	n = object.n;
}

Plane& Plane::operator=(const Plane& rhs)
{
	a = rhs.a; 
	n = rhs.n;

	return *this; 
}

std::string Plane::to_string() const
{
	std::string retval = "( ";

	retval.append(a.to_string() + ", ");
	retval.append(n.to_string() + ")");

	return retval;
}

bool Plane::hit(const Ray& ray, float& t, ShadeInfo& s) const
{
	Point3D ray_o = ray.o;
	Vector3D oa_diff = ray_o - a;

	t = -(oa_diff * n)/(ray.d * n); 
	
	if (t > 0)
		return true;
	else
		return false;

}

BBox Plane::getBBox() const
{
	return BBox();
}


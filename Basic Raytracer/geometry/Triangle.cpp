#include "Triangle.hpp"
#include "../utilities/BBox.hpp"

Triangle::Triangle()
{
	v0 = v1 = v2 = Point3D();
}

Triangle::Triangle(const Point3D& _v0, const Point3D& _v1, const Point3D& _v2)
{
	v0 = _v0;
	v1 = _v1;
	v2 = _v2;
}

Triangle::Triangle(const Triangle& object)
{
	v0 = object.v0;
	v1 = object.v1;
	v2 = object.v2;
}

Triangle& Triangle::operator=(const Triangle& rhs)
{
	v0 = rhs.v0;
	v1 = rhs.v1;
	v2 = rhs.v2;

	return *this; 
}

std::string Triangle::to_string() const
{
	std::string retval = "(";

	retval.append(v0.to_string() + ", ");
	retval.append(v1.to_string() + ", ");
	retval.append(v2.to_string() + ")");

	return retval;
}

BBox Triangle::getBBox() const
{
	Point3D P0 = min(v0, min(v1, v2));
	Point3D P1 = max(v0, max(v1, v2));

	return BBox(P0, P1);
}


#include "Point3D.hpp"
#include "Vector3D.hpp"
#include <cstdint>

//Constructors
Point3D::Point3D()
{
	x = y = z = 0;
}

Point3D::Point3D(float c)
{
	x = y = z = c;
}

Point3D::Point3D(float x, float y, float z)
{
	this->x = x;
	this->y = y; 
	this->z = z;
}


//String Representation
std::string Point3D::to_string() const
{
	std::string retval = "("; 

	retval.append(std::to_string(x) + ", ");
	retval.append(std::to_string(y) + ", ");
	retval.append(std::to_string(z) + ")");

	return retval;
}

//Arithmetic
Point3D Point3D::operator-() const
{
	return Point3D(-x, -y, -z);
}

Vector3D Point3D::operator-(const Point3D& p) const
{
	return Vector3D((double) x - p.x, 
					(double) y - p.y, 
					(double) z - p.z);
}

Point3D Point3D::operator+(const Vector3D& v) const
{
	return Point3D((float) x + v.x, (float) y + v.y, (float) z + v.z);
}

Point3D Point3D::operator-(const Vector3D& v) const
{
	return Point3D((float) x - v.x, (float) y - v.y, (float) z - v.z);
}

Point3D Point3D::operator*(const float s) const
{
	return Point3D(x * s, y * s, z * s);
}

//Distance between points
float Point3D::d_squared(const Point3D& p) const
{
	return (powf((p.x - x), 2) + powf((p.y - y), 2) + powf((p.z - z), 2));
}

float Point3D::distance(const Point3D& p) const
{
	return powf(d_squared(p), 0.5);
}

Point3D operator*(const float s, const Point3D& pt)
{
	return Point3D(pt.x * s, pt.y * s, pt.z * s);
}

Point3D min(const Point3D& a, const Point3D& b)
{
	float newX = a.x <= b.x ? a.x : b.x; 
	float newY = a.y <= b.y ? a.y : b.y;
	float newZ = a.z <= b.z ? a.z : b.z;

	return Point3D(newX, newY, newZ);
}

Point3D max(const Point3D& a, const Point3D& b)
{
	float newX = a.x >= b.x ? a.x : b.x;
	float newY = a.y >= b.y ? a.y : b.y;
	float newZ = a.z >= b.z ? a.z : b.z;

	return Point3D(newX, newY, newZ);
}

#include "Vector3D.hpp"
#include "Point3D.hpp"
#include <cstdint>


Vector3D::Vector3D()
{
    x = y = z = 0;
}

Vector3D::Vector3D(double c)
{
    x = y = z = c;
}

Vector3D::Vector3D(double _x, double _y, double _z)
{
    x = _x; 
    y = _y; 
    z = _z;
}

Vector3D::Vector3D(const Point3D  &p)
{
    x = (double)p.x;
    y = (double)p.y;
    z = (double)p.z;
}

Vector3D& Vector3D::operator=(const Point3D& rhs)
{
    x = (double)rhs.x;
    y = (double)rhs.y;
    z = (double)rhs.z;

    return *this;
}


//String Representation 
std::string Vector3D::to_string() const
{
    std::string retVal = "(";

    retVal.append(std::to_string(x) + ", ");
    retVal.append(std::to_string(y) + ", ");
    retVal.append(std::to_string(z));

    retVal.append(")");
    return retVal;
}


//Arithmetic
Vector3D Vector3D::operator-() const
{
    return Vector3D(-x, -y, -z);
}

Vector3D Vector3D::operator+(const Vector3D& v) const
{
    return Vector3D(x + v.x, 
                    y + v.y, 
                    z + v.z );
}

Vector3D& Vector3D::operator+=(const Vector3D& v)
{
    x += v.x; 
    y += v.y; 
    z += v.z; 

    return *this;
}

Vector3D Vector3D::operator-(const Vector3D& v) const
{
    return Vector3D(x - v.x,
                    y - v.y,
                    z - v.z);
}

Vector3D Vector3D::operator-=(const Vector3D& v)
{
    x -= v.x;
    y -= v.y;
    z -= v.z;

    return *this; 
}

//Scalings
Vector3D Vector3D::operator*(const double a) const
{
    return Vector3D(x*a, y*a, z*a);
}

Vector3D Vector3D::operator/(const double a) const
{
    return Vector3D(x/a, y/a, z/a);
}

void Vector3D::normalize()
{
    double len = (x*x + y*y + z*z);
    len = pow(len, 0.5);
    x /= len; 
    y /= len;
    z /= len; 
}

double Vector3D::length() const
{
    return pow((x * x + y * y + z * z), 0.5);
}

double Vector3D::len_squared() const
{
    return (x * x + y * y + z * z);
}

//dot product
double Vector3D::operator*(const Vector3D& b) const
{
    return (x * b.x) + (y * b.y) + (z * b.z);
}

//cross product
Vector3D Vector3D::operator^(const Vector3D& v) const
{
    double cp_x = (y * v.z) - (z * v.y);
    double cp_y = (z * v.x) - (x * v.z);
    double cp_z = (x * v.y) - (y * v.x);

    return Vector3D(cp_x, cp_y, cp_z);
}

//Scaling 
Vector3D operator*(const double a, const Vector3D& v)
{
    return Vector3D(v.x * a, v.y * a, v.z * a);
}

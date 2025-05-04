#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <floatobject.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject pointer to a Python object (expected to be a list)
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;
    const char *type;

    fflush(stdout);
    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = ((PyListObject *)p)->ob_item[i];
        type = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
        else if (strcmp(type, "float") == 0)
            print_python_float(item);
    }
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: PyObject pointer to a Python object (expected to be bytes)
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    fflush(stdout);
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    string = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %ld bytes:", size + 1 > 10 ? 10 : size + 1);
    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02x", string[i] & 0xff);
    printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject pointer to a Python object (expected to be a float)
 */
void print_python_float(PyObject *p)
{
    double value;

    fflush(stdout);
    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    printf("  value: %s\n", PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

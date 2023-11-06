#include <python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;

	PyListObject *obj = (PyListObject *)p;

	printf("[*] size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}

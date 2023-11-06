#include <python.h>

/**
 * print_python_list_info - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_size(p);
	Py_ssize_t allocated = PyList_GET_SIZE(p);
	Py_ssize_t i;
	char *item_type_name;

	printf("Size of the Python List = %ld\n", size);
	printf("Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		PyObject *item_type = PyObject_Type(item);
		*item_type_name = Py_TYPE(item_type)->tp_name;
		printf("Element %ld: %s\n", i, item_type_name);
	}
}

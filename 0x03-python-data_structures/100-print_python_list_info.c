#include <Python.h>

/**
 * print_python_list_info - gives data of the PyListObject
 * @p: the PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	int size = 0;
	int i = 0;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	while (i < size)
	{
		printf("Element %d: %s\n",
				i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}

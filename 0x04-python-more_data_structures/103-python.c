#include <Python.h>

/**
 * print_python_list - print basic info about Python lists
 * @p; the PyObject
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	int size = 0;
	PyObject *item;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			i++;
		}
	}	
}

/**
 * print_python_bytes - print basic info about Python byte
 * @p: the PyObject
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	int size = 0, i = 0;
	char *string = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &string, &size) != -1)
	{
		printf("  size: %d\n", size);
		printf("  trying string: %s\n", string);
		printf("  first %d bytes:", size < 10 ? size + 1 : 10);
		while (i < size + 1 && i < 10)
		{
			printf(" %02hhx", string[i]);
			i++;
		}
		printf("\n");
	}
}

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *print_list - prints all ellements of a listint_t list
 *@h:pointer to head of listint_t list
 *Return:number of nodes
 *
 *
 */
size_t	print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /*number of nodes*/

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->next);
		n++;
	}
	return (n);
}

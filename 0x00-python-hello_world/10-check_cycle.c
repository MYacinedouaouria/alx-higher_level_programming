#include "lists.h"
/**
 *check_cycle - checks if a singly linked listint_t list has a cycle in it
 *@list: the list to be checked
 *Return:0 if ther is no cycle, else 1 if the is a cycle
 *
 *
 */
int	check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *next;

	if (list == NULL)
		return (0);

	current = list;
	while (current != NULL)
	{
		next = current->next;
		while (next != NULL)
		{
			if (next == current)
			{
				return (1);
			}
			next = next->next;
		}
		current = current->next;
	}

	return (0);
}

#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks the cycliest of list
 * @list: pointer to list
 * @Retrun : 1 if cyclist , 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast -> next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

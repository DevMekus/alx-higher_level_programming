#include "list.h"
/**
 * free_listint - Frees the Memory of the linked list
 * @*head - Pointer to the memory to be freed
 */

void free_listint(listint_t *head)
{
	free(head);
}

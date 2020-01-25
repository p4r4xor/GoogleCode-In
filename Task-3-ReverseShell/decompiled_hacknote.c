//I'll upload all the following codes on github for reference.

unsigned int SUB_printNote() // this is the print note function
{
  int index; // [esp+4h] [ebp-14h]
  char buf[4]; // [esp+8h] [ebp-10h]
  unsigned int v3; // [esp+Ch] [ebp-Ch]
 
  v3 = __readgsdword(0x14u);
  printf("Index :");
  read(0, buf, 4u);
  index = atoi(buf);
  if ( index < 0 || index >= noteCnt )
  {
    puts("Out of bound!");
    _exit(0);
  }
  if ( ptr[index] )
    (*ptr[index])(ptr[index]);   // at this line,we can see how the function pointer is used.
                                 // So, the parameter is the function pointer itself!
  return __readgsdword(0x14u) ^ v3;
}

unsigned int SUB_delete() // this is the delete function
{
  int index; // [esp+4h] [ebp-14h]
  char buf[4]; // [esp+8h] [ebp-10h]
  unsigned int v3; // [esp+Ch] [ebp-Ch]
 
  v3 = __readgsdword(0x14u);
  printf("Index :");
  read(0, buf, 4u);
  index = atoi(buf);
  if ( index < 0 || index >= noteCnt )
  {
    puts("Out of bound!");
    _exit(0);
  }                                            // In the delete function, there is a vulnerability. // After deletion, it does not clear 'ptr[index]'.

  //Which means that we can double free the chunk!!!
  if ( ptr[index] )
  {
    free(*(ptr[index] + 1));                    // content
    free(ptr[index]);                           // main chunk
    puts("Success");
  }
  return __readgsdword(0x14u) ^ v3;
}


unsigned int SUB_add() //this is the add note function
{
  _DWORD *v0; // ebx
  signed int i; // [esp+Ch] [ebp-1Ch]
  int size; // [esp+10h] [ebp-18h]
  char buf[8]; // [esp+14h] [ebp-14h]
  unsigned int v5; // [esp+1Ch] [ebp-Ch]
 
  v5 = __readgsdword(0x14u);
  if ( noteCnt <= 5 )
  {
    for ( i = 0; i <= 4; ++i )
    {
      if ( !ptr[i] )                            // when ptr[i] is empty
      {
        ptr[i] = malloc(8u);
        if ( !ptr[i] )
        {
          puts("Alloca Error");
          exit(-1);
        }
        *ptr[i] = SUB_func;                     // func ptr
        printf("Note size :");
        read(0, buf, 8u);
        size = atoi(buf);
        v0 = ptr[i];
        v0[1] = malloc(size);
        if ( !*(ptr[i] + 1) )
        {
          puts("Alloca Error");
          exit(-1);
        }
        printf("Content :");
        read(0, *(ptr[i] + 1), size);
        puts("Success !");
        ++noteCnt;
        return __readgsdword(0x14u) ^ v5;
      }
    }
  }
  else
  {
    puts("Full");
  }
  return __readgsdword(0x14u) ^ v5;
}

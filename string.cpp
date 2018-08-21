#pragma once
#include <string.h>
#include <assert.h>

class String {
    public:
        String() : data(new char[1]) {
            *data = '\0';
        }

        String(const char* str) : data(new char[strlen(str) + 1]) {
            strcpy(data, str);
        }

        String(const String& rhs) : data(new char[rhs.size() + 1]) {
                strcpy(data, rhs.c_str());
        }

        ~String() noexcept {
            delete[] data;
        }

        String& operator=(const String& rhs) {
            if (

        



                    


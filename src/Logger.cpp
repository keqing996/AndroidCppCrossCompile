#include "Logger.h"

#include <android/log.h>

void LogCatInfo(const char* tag, const char* message)
{
    __android_log_print(ANDROID_LOG_INFO, tag, "%s", message);
}

void LogCatError(const char* tag, const char* message)
{
    __android_log_print(ANDROID_LOG_ERROR, tag, "%s", message);
}

void LogCatWarning(const char* tag, const char* message)
{
    __android_log_print(ANDROID_LOG_WARN, tag, "%s", message);
}
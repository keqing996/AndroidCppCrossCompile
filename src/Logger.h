#pragma once

constexpr const char* LogTag = "HelloWorld";

void LogCatInfo(const char* tag, const char* message);

void LogCatError(const char* tag, const char* message);

void LogCatWarning(const char* tag, const char* message);
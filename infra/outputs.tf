output "jenkins_public_ip" {
  description = "Public IP of Jenkins server"
  value       = aws_instance.jenkins_server.public_ip
}

output "app_server_public_ip" {
  description = "Public IP of App server"
  value       = aws_instance.app_server.public_ip
}
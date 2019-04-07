provider "kubernetes" {
  host = "http://127.0.0.1:8001"
}

resource "kubernetes_replication_controller" "openwisp" {
  metadata {
    name = "openwisp"

    labels {
      App = "openwisp"
    }
  }

  spec {
    replicas = 3

    selector {
      App = "openwisp"
    }

    template {
      metadata {
        labels {
          App = "openwisp"
        }
      }

      spec {
        container {
          image   = "atb00ker/ready-to-run:openwisp-web"
          name    = "openwisp-web"
          command = ["/opt/openwisp2/init_command.sh"]

          port {
            container_port = 8000
          }

          env {
            name  = "DJANGO_REDIS_HOST"
            value = "localhost"
          }
        }

        container {
          image = "redis:alpine"
          name  = "redis"
        }
      }
    }
  }
}

resource "kubernetes_service" "openwisp" {
  metadata {
    name = "openwisp"
  }

  spec {
    selector {
      App = "${kubernetes_replication_controller.openwisp.metadata.0.labels.App}"
    }

    port {
      port        = 8000
      target_port = 8000
    }

    external_ips = ["192.168.1.6"]
    type         = "LoadBalancer"
  }
}
